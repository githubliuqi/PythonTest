#!/bin/sh

# 当前路径  
Cur_Dir=$(cd `dirname $0`; pwd)
echo 当前路径 ${Cur_Dir}
cd ${Cur_Dir}

input_dir=$1

#
# 计算文件大小
if [ -d $input_dir ];then
    cd $input_dir
fi

# 记录hash结果到hash.sh同级目录下info.txt
info_file="$Cur_Dir/info.txt"
rm -f "$info_file"
echo "********************* 请查看文件大小是否异常 ************************" >>${info_file}
#echo "" >>${conf_build_log_file}
#du -h -d1 ./* >>${conf_build_log_file}

# deal with file
function doFile(){
showFileInfo $1
#checkPrivateApi $1
}

# print file info
function showFileInfo(){

file=$1
echo "">>${info_file}
#echo "${file##*/}" >>${info_file}
echo "${file:${#input_dir}}" >>${info_file}


file_size=$(ls -l $1 | awk '{print $5}')
file_md5=$(md5 $1 | awk '{print $4}')
file_sha1=$(shasum $1 | awk '{print $1}')

echo "size = ${file_size} Byte " >>${info_file}
if [ -d $1 ] ;then
    break
else
    echo "MD5  = ${file_md5} " >>${info_file}
    echo "SHA1 = ${file_sha1} " >>${info_file}
fi
#echo "">>${info_file}

}

# 遍历dir
function walkDir(){

if [ ! -d $1 ];then
   doFile $1
   exit 0
fi
for element in `ls $1`
do
sub_file="$1/${element}"
    if [ -d ${sub_file} ];then
#        if [ -d $sub_file ];then
#          continue
#        fi
         walkDir $sub_file
    else
#    echo "$sub_file"
        doFile $sub_file
#    if [ "${sub_file##*.}"x = "a"x ]||[ "${sub_file##*.}"x = "ipa"x ];then
#       doFile $sub_file
#    fi
    fi
done
}


walkDir "$input_dir"


