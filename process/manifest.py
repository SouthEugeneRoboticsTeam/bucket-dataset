import glob, os, re, json

def atoi(text):
    return int(text) if text.isdigit() else text

def natural_keys(text):
    return [ atoi(c) for c in re.split('(\d+)', text) ]

def generate_manifest(dir, pattern, manifest):
    files = glob.glob(os.path.join(dir, pattern))
    data = []

    for pathAndFilename in files:
        data.append(pathAndFilename.split('/')[-1])

    data.sort(key=natural_keys)

    with open(manifest, 'w') as outfile:
        json.dump(data, outfile)

generate_manifest(r'../imageset_2', r'*', r'../imageset_2/_manifest.json')
