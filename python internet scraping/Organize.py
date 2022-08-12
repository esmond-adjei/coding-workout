import os, shutil

def organize(sourceDir,sinkDir, keyword = ["."], form = "mp4"):
    """
        1. Navigate to directory
        2. Make new folder/directory from keyword if folder doesn't exit
        3. Identify all non folders (files) within the current directory with keyword in their name
        4. Move those files to the destination folder(subfolder that was created from keyword)
            *when a '.' is given as 'keyword', 'format' of file is used as name of created directory
    """
    os.chdir(sourceDir)                 # change to the given directory
    print("--> source folder: ", os.getcwd())
    if not os.path.exists(sinkDir):     # if subfolder doesn't exit then...
        os.mkdir(sinkDir)               # make subfolder within current directory

    videoForm = ("mp4","mkv","wmv","ts","avi","flv")
    #pictureForm = ("jpeg","jpg","png","jfif","pjpeg","pjp","svg","webp")       #...talk about this later
    if form == 'v':
        form = videoForm
    moveSuccess = 0         # counter
    for f in os.listdir():  # loop through current
        if not os.path.isdir(f) and f[-3:] in form:     # check if object is not folder(file) and if extension equals format
            for key in keyword:
                try:        # try changing the filename and key to lower case for comparison
                    key = key.lower()
                    F = f.lower()
                except:
                    pass
                if key in F:                    # check if keyword is in filename
                    shutil.move(sourceDir +"/"+ f, sinkDir +"/"+ f) # move from souce(current directory) to destination(subfolder directory)
                    moveSuccess += 1
    print(f"\t______ALL DONE!_______\n\t| {moveSuccess} files moved from:\n\t| {sourceDir.upper()} -->> {sinkDir.upper()}")


if __name__=="__main__":
	sourceFolder = input("1/4>> Paste Path of source Folder here: ")
	sourceFolder.replace("\\","/")                              # replace "\" with "/" in case of Windows OS
	destFolder = input("2/4>> Name of folder to save to: ")
	searchKeyword = input("3/4>> Specify keyword (default will select all files): ").split()
	fileFormat = input("4/4>> Specify file format (default is all video format eg: 'v' for video): ")

	organize(sourceFolder,destFolder,searchKeyword,fileFormat)             # inputs are ready, call function