for g in *.gif; do
    n=$(echo $g |sed 's/\.gif$/.mkv/')
    echo "moving $g to $n"
    ffmpeg -i $g $n
done
