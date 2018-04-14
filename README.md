# PlotCloneStream
If you sampling clone data more than once from one samples, this python script would help you plot a dynamic clone stream.

# Usage
```
./PlotStreamClone.py -h

usage: python ParseIgBLAST.py -i infile1,infile2,infile3,... -o1 outname -o2 outfigure -d outdir

Plot CDR3 stream over time

optional arguments:
  -h, --help            show this help message and exit
  -i INFILE, --infile INFILE
                        Input seq.merge.txt, splited by comma
  -d OUTDIR, --outdir OUTDIR
                        Output file director
  -o1 OUTFILE, --outfile OUTFILE
                        Output tab format file: CDR3 index num1 num2 ...
  -o2 OUTFIGURE, --outfigure OUTFIGURE
                        Output figure
  -v, --version         show program's version number and exit

Created by WangCR. April 10, 2018
```

# Input files example
*Clone1.txt, Clone2.txt, Clone3.txt*

Splited by tab, format as follow:
```
CDR3_nt_seq CDR3_aa_seq ID  recombination_info  ....
```
recombination_info record is:
```
V;D;J;chaintype;stop_codon;frame_info;productive;strand
```

# Output file
```
#CDR3_nt_seq Rank  num1sample  num2sample  num3sample  per1sample  per2sample  per3sample
CAGCAATATAGCAGCTATCCTCTCACG     0       1319    1463    12229   1.3891  2.2773  8.0911
CAGCAATATAACAACTATCCGTACACG     1       700     411     11258   0.7372  0.6398  7.4486
CAGCAATATAACAACTATCCTCGGACG     2       245     220     9192    0.258   0.3424  6.0817
CAGCAATATAACAGCTATCCTCTCACG     3       1821    1572    5302    1.9178  2.447   3.508
...
```

# Figure
// ![Clone Stream for percemtage]
