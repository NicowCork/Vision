import shutil 
import sys




def check_disk_usage(disk, min_absolute, min_percent):
    
    answer = 0

    du = shutil.disk_usage(disk)
    


    percent_free = 100 * du.free / du.total
    gigabytes_free = du.free / 2**30
    print(du.free)
    print(du.total)

    if percent_free < min_percent or gigabytes_free < min_absolute:
            return False
    else:
        answer = percent_free
        return True


if not check_disk_usage("/", 2, 10): 
    print("ERROR: Not enough disk space")
    sys.exit(1)

#print("Everything ok")
#print("You have: {}% available on your disk.".format(answer))
#sys.exit(0)