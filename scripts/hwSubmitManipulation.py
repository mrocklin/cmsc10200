import os

from glob import glob


username = lambda dir: dir.split('_')[1]
dirname = lambda s: os.path.splitext(s)[0]


def joinFiles(filenames):
  def header(filename):
    eqstring = '='*60+'\n'
    return '\n'+eqstring+eqstring+filename+'\n'+eqstring+eqstring

  files = [open(filename) for filename in filenames]
  texts = [file.read() for file in files]
  fulltext = '\n'.join([header(fn)+text for fn, text in zip(filenames,texts)])
  for file in files:
    file.close()
  return fulltext

def createJoinedFiles():
  files = glob('*') #get everything in hw directory
  def cnet(filename):
    words = filename.split('_')
    if filename[:2]!='HW' or len(words)<=2:
      return None
    return words[1]
  cnetids = set(map(cnet, files))

  for cnetid in cnetids:
    if not cnetid:
      pass
    myfiles = glob('HW*_%s*/*.java'%cnetid)
    myfiles.sort()
    myfiles = [file for file in myfiles if 'Data.java' not in file]
    printfile = open('joined_%s.txt'%cnetid, 'w')
    printfile.write(joinFiles(myfiles))
    printfile.close()



def unjar():
  jarfiles = glob('*.jar')

  for jfile in jarfiles:
    dir = dirname(jfile)
    os.mkdir(dir)
    os.system('mv %s %s'%(jfile,dir));
    os.chdir(dir);
    os.system('jar xf %s'%jfile);
    os.chdir('..');

def go():
  jarfiles = glob('*.jar')

  for jfile in jarfiles:
    dir = dirname(jfile)
    os.mkdir(dir)
    os.system('mv %s %s'%(jfile,dir));
    os.chdir(dir);
    os.system('jar xf %s'%jfile);
    os.chdir('..');
#  txtfiles = [f for f in glob('*.txt') if len(f.split('_'))>2]
#  txtfiles.sort()
#  for txt in txtfiles:
#    os.system('enscript -r2 -P ry160b-2 '+txt)

def output():
  dirs = [x for x in sorted(glob('HW5_*')) if '.txt' not in x and '.html' not in x]
  homeworkdir = '/home/mrocklin/Downloads/hw5/'
  for dir in dirs:
    os.chdir(homeworkdir+dir)
    pipe = os.popen('java Data')
    f = open(homeworkdir+'output_'+username(dir)+'.txt', 'w')
    f.write(pipe.read())
    f.close();

