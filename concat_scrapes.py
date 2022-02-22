import glob, os, subprocess

path = "C:\\Users\\Home\\projects\\helm"
os.chdir(path)

outfilename = path + "\\compiled-config\\prometheus-additional.yaml"

def concatenate_scrapes():
  with open(outfilename, 'w') as outfile:
    outfile.seek(0)
    for filename in glob.glob('scrape-config\\*.yaml'):
      if filename == outfilename:
        continue
      with open(filename, 'r') as readfile:
        for line in readfile:
          if not line.isspace():
            outfile.write(line)

def create_sectet():
  os.system("kubectl.exe create secret generic additional-scrape-configs --from-file=" + outfilename + " --dry-run=client -oyaml > C:\\Users\\Home\\projects\\helm\\K8s-secret\\additional-scrape-configs.yaml")

concatenate_scrapes()
create_sectet()