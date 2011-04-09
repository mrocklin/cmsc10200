dirname = lambda s: s[:4]+s[4:].split('_')[0]

for jfile in jarfiles:
  dir = dirname(jfile)
  os.mkdir(dir)
  os.system('mv %s %s'%(jfile,dir));
  os.chdir(dir);
  os.system('jar xf %s'%jfile);
  os.chdir('..');

txtfiles = [f for f in glob('*.txt') if len(f.split('_'))>2]
for txt in txtfiles:
  os.system('enscript -r2 -P ry160b-2 '+txt)

