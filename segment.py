# -*- coding: utf-8 -*-
import sys
reload(sys)
import argparse
import chardet
sys.setdefaultencoding('utf-8')
#读取语料
def GetCorpusDict(corpus):
    f=open(corpus)
    corpus_dict={}
    for line in f.readlines():
        key=line.strip().decode('utf-8')
        if not corpus_dict.get(key):
            corpus_dict[key]=1
    return corpus_dict
#前向最大匹配
def MaxMatch(corpus_dict,cand_text,max_len):
    text= cand_text.decode('utf-8')
    if len(cand_text)< max_len:max_len=len(cand_text)
    result=[]
    cands_size = len(text)
    while cands_size>0 :
        cand = text[0:max_len]
        while cand not in corpus_dict:
            if len(cand)==1:break
            cand=cand[0:len(cand)-1]
        result.append(cand)
        text = text[len(cand):]
        cands_size = len(text)
    return result
#后向最大匹配
def InverseMaxMatch(corpus_dict,cand_text,max_len):
    text= cand_text.decode('utf-8')
    if len(cand_text)< max_len:max_len=len(cand_text)
    result=[]
    cands_size = len(text)
    while cands_size>0 :
        cand = text[-max_len:]
        while cand not in corpus_dict:
            if len(cand)==1:break
            cand=cand[1:]
        result.append(cand)
        text = text[0:(len(text)-len(cand))]
        cands_size = len(text)
    return result
def run(args):
    corpus_dict=GetCorpusDict(args.corpus)
    if args.way=="forword":
        res=MaxMatch(corpus_dict,args.text,args.max_len)
    else:
        res=InverseMaxMatch(corpus_dict,args.text,args.max_len)
    ff=open(args.output,'w')
    for ks in res:
        ff.write(ks+'\t')
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-c","--corpus",help="corpus")
    parser.add_argument("-t","--text",help="text")
    parser.add_argument("-l","--max_len",help="max_len")
    parser.add_argument("-i","--way",help="forword or inverse")
    parser.add_argument("-o","--output",help="output")
    args = parser.parse_args()
    run(args)
#corpus_dict=GetCorpusDict("test_data")
#ss=MaxMatch(corpus_dict,"北京海淀",3)
#print ss[0],ss[1]
