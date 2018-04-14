#!/user/bin/python
"""
python .py -i infile1,infile2,infile3,... -d outdir -o1 outname -o2 outfigure
"""
from __future__ import division
import os,sys,csv
import argparse
import matplotlib.pyplot as plt
from matplotlib import colors
import matplotlib.cm as cmx
import numpy as np

def main():
	files = infiles.split(",")
	filenum = len(files)
	cdr3list,xlist,data,data2 = [],[],[],[]
	numdict = {}
	dict2 = {}
	samplenum = []
	for ind1,file in enumerate(files):
		handle = open(file,'rU')
		reader = csv.reader(handle,delimiter='\t')
		allnum = 0
		for rec in reader:
			if rec[0].startswith("N/A"):
				continue
			recom = rec[3].split(";")
			if recom[4]=="Yes" and recom[6]=="No":
				continue
			if rec[0] not in cdr3list:
				cdr3list.append(rec[0])
			numdict.setdefault(cdr3list.index(rec[0]),[0]*filenum)[ind1] += 1
			allnum += 1
		samplenum.append(allnum)
		handle.close()
	xlist = range(filenum)
	for key in numdict.keys():
		mysum = sum(numdict[key])
		myaver = np.mean(numdict[key])
		dict2[key] = [myaver]
	index = 0
	for key,val in sorted(dict2.items(),key=lambda e:e[1],reverse=True):
		result = [round(100*x/samplenum[inde],4) for inde,x in enumerate(numdict[key])]
		out1.writerow([cdr3list[key],index]+numdict[key]+result)
		if np.mean(numdict[key])>100 and np.min(numdict[key])>0:
			data.append(numdict[key])
			data2.append(result)
		index += 1

	fig,ax = plt.subplots()
	ax.stackplot(xlist,data,alpha=.7,linewidth=.2)#,colors=colors_list(col="bwr",N=len(data)*2))
	plt.savefig('%s/%s.num.png'%(outdir,outfig),format="png")
	fig,ax = plt.subplots()
	ax.stackplot(xlist,data2,alpha=.7,linewidth=.2)#,colors=colors_list(col="bwr",N=len(data)*2))
	plt.savefig('%s/%s.per.png'%(outdir,outfig),format="png")

if __name__=='__main__':
	parser = argparse.ArgumentParser(prog='python ParseIgBLAST.py',usage='%(prog)s -i infile1,infile2,infile3,... -o1 outname -o2 outfigure -d outdir',description = 'Plot CDR3 stream over time',epilog = 'Created by WangCR. April 10, 2018')
	parser.add_argument('-i','--infile',help='Input seq.merge.txt, splited by comma')
	parser.add_argument('-d','--outdir',default=".",help='Output file director')
	parser.add_argument('-o1','--outfile',default="CDR3stream.txt",help='Output tab format file: CDR3 index num1 num2 ...')
	parser.add_argument('-o2','--outfigure',default="CDR3stream.png",help='Output figure')
	parser.add_argument('-v','--version', action='version', version='Copyright (c) 10/4/2018, created by WangChengrui, version 1.0')
	args = parser.parse_args()
	infiles = args.infile
	outdir = args.outdir
	outname = args.outfile
	outfig = args.outfigure
	os.system("mkdir -p %s"%outdir)

	out1 = csv.writer(open('%s/%s'%(outdir,outname),'wb'),delimiter='\t')
	main()
