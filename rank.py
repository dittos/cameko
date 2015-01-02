import os
import sys
import shutil
import animeface
from PIL import Image

min_size = 50

def calc_score(faces):
    score = 0
    efflen = 0
    print faces
    for face in faces:
        if max(face.face.pos.width, face.face.pos.height) < min_size:
            continue
        efflen += 1
        score += face.face.pos.width * face.face.pos.height * face.likelihood
    return (efflen, score)

def main():
    dir_path = sys.argv[1]
    face_dir = os.path.join(dir_path, 'face')
    shutil.rmtree(face_dir, ignore_errors=True)
    try:
        os.makedirs(face_dir)
    except:
        pass

    result = []
    for filename in os.listdir(dir_path):
        if not filename.endswith('.jpg'):
            continue
        print filename
        path = os.path.join(dir_path, filename)
        im = Image.open(path)
        faces = animeface.detect(im, analyze=False)
        if faces:
            result.append((filename, calc_score(faces)))

    result.sort(key=lambda (_, score): score, reverse=True)

    for rank, t in enumerate(result):
        filename, score = t
        path = os.path.join(dir_path, filename)
        os.symlink(os.path.abspath(path), os.path.join(face_dir, '%d_%03d_%s' % (score[0], rank, filename)))

if __name__ == '__main__':
    main()
