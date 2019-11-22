#! /bin/bash

srcExt="mp3"
destExt="wav"

srcDir="./**"
destDir="dest"

opts=""

for fd in ./*; do
	if [ -d "$fd" ]; then
		for filename in ./**/*.$srcExt; do
			if [ -f "$filename" ]; then

				if [ ! -d "$destDir"/"$fd" ]; then
				    mkdir -p "$destDir"/"$fd"
			    fi
			fi
		done
	fi
done

for fd in ./*; do
	if [ -d "$fd" ]; then
		for filename in ./"$fd"/*.$srcExt; do
			if [ -f "$filename" ]; then

		        basePath=${filename%.*}
		        baseName=${basePath##*/}

		        baseNameR="${baseName// /_}" 

		        ffmpeg -i "$filename" $opts ./"$destDir"/"$fd"/"$baseNameR"."$destExt"
			fi
		done
	fi
done

echo "Conversion from ${srcExt} to ${destExt} complete!"