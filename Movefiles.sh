IFS_BAK=$IFS
IFS="
"
string=""
for line in $NAUTILUS_SCRIPT_SELECTED_FILE_PATHS; do
        string="$string  $line"
        # notify-send $line
done
full_path="/home/"$USER"/Desktop/"file.py
python $full_path $string
