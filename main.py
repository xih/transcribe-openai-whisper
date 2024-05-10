import datetime
import whisper
import os

# pip install git+https://github.com/openai/whisper.git
# ran into hella issues - the solution is python3 main.py :facepalm:

# 5/10/2024
# to run the script
# 0. change foldername variable to your specific path with MP4 files
# 1. pipenv shell
# 2. python3 main.py

def findAllMp4sInFolder(folder_path):
  mp4_files = []
  for file in os.listdir(folder_path):
      if file.endswith(".mp4"):
          mp4_files.append(file)
  return mp4_files

def main2():
  folder = "/Users/dennis/Documents/01 - muro media/references/rentingsf2" 
  print(findAllMp4sInFolder(folder))


def generateCaptionsFromFolder(folderName):
  model = whisper.load_model("base")


  mp4List = findAllMp4sInFolder(folderName)

  # Define the maximum characters per line
  max_chars_per_line = 140


  for mp4FileName in mp4List:
    fullMp4Path = folderName + "/" + mp4FileName
    result = model.transcribe(fullMp4Path)


    transcriptionPath = folderName + "/" +  mp4FileName.replace(".mp4", "") + "caption_" + ".txt" 

    # transcriptionPathLocal = "caption_" + mp4FileName + ".txt" 

    with open(transcriptionPath, "w") as file:
    # file.write(result["text"])

      words = result["text"].split()
      lines = []
      current_line = ""
      
      for word in words:
          if len(current_line) + len(word) + 1 <= max_chars_per_line:
              current_line += word + " "
          else:
              lines.append(current_line)
              current_line = word + " "
      
      if current_line:
          lines.append(current_line)
      
      file.write('\n'.join(lines))
      print("file written succesfully")
     
   

def main():
  # filename = "2024-03-14_@rentingsf_7346323152324267310.mp4"
  # filename2 = "/Users/dennis/Documents/01 - muro media/references/rentingsf2/2024-03-14_@rentingsf_7346323152324267310.mp4"
  # folder = "/Users/dennis/Documents/01 - muro media/references/rentingsf2" 
  folderName = "/Users/dennis/Documents/01 - muro media/references/sf apartment plug"
  folderName2 = "/Users/dennis/Documents/01 - muro media/references/hans lorei design"
  generateCaptionsFromFolder(folderName2)




if __name__ == "__main__":
  main()