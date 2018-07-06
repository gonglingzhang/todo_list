# -*-encoding:utf-8-*-
# create palette to improve the quality of gif
import os,sys
input_file = sys.argv[1]
def make_palette(input_file):
    os.system('ffmpeg -y -i '+ input_file + ' -vf fps=10,scale=800:-1:flags=lanczos,palettegen /home/glz/视频/palette.png ')


if __name__ == '__main__':
    make_palette(input_file)

