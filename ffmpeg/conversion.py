# -*-encoding:utf-8-*-
# Convert mp4 to gif, use palette to imporve quality

import os,sys
input_file = sys.argv[1]
output_file = sys.argv[2]
def cut(input_file, output_file):
    os.system('ffmpeg -i ' + input_file + ' -i /home/glz/视频/palette.png -filter_complex \
		"fps=10,scale=800:-1:flags=lanczos[x];[x][1:v]paletteuse" ' + output_file)


if __name__ == '__main__':
    cut(input_file, output_file)
