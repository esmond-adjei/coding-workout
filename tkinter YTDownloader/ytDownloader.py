from pytube import YouTube as YT
import tkinter as tk

WIDTH = 400
HEIGHT = 150
ENTRY_WIDTH = 50 
TITLE = "Youtube Downloader"
BG = "#ff6f00"
ROW_1 = 1
ROW_2 = 2
ROW_3 = 3
ROW_4 = 4
COL_1 = 1
COL_2 = 2


class YouTubeDownloader:
	
	def __init__(self):
		# window configuration :: width, height, background color
		self.window = tk.Tk()
		self.window.geometry(f"{WIDTH}x{HEIGHT}")
		self.window.configure(bg=BG)
		self.window.title(TITLE)

		#create labels
		self.link_label = tk.Label(self.window, text = "Download link", bg=BG)
		self.name_label = tk.Label(self.window, text = "Save File as", bg=BG)
		self.path_label = tk.Label(self.window, text = "Save File Path", bg=BG)
		self.ext_label = tk.Label(self.window, text = "File extension", bg=BG)
		self.link_label.grid(column = COL_1, row = ROW_1)
		self.name_label.grid(column = COL_1, row = ROW_2)
		self.path_label.grid(column = COL_1, row = ROW_3)
		self.ext_label.grid(column = COL_1, row = ROW_4)

		#create Entry
		self.link_entry = tk.Entry(master = self.window, width = ENTRY_WIDTH)
		self.name_entry = tk.Entry(master = self.window, width = ENTRY_WIDTH)
		self.path_entry = tk.Entry(master = self.window, width = ENTRY_WIDTH)
		self.ext_entry = tk.Entry(master = self.window, width = ENTRY_WIDTH)
		self.link_entry.grid(column = COL_2, row = ROW_1)
		self.name_entry.grid(column = COL_2, row = ROW_2)
		self.path_entry.grid(column = COL_2, row = ROW_3)
		self.ext_entry.grid(column = COL_2, row = ROW_4)

		# Create Dowload Button
		self.download_button = tk.Button(self.window, text = "Download", command = self.__get_link, bg="#ffee11")
		self.download_button.grid(column = COL_2, row = ROW_4+2)

		return


	def __downloader(self, link, save_path = "c:/users/hp/desktop", save_name = "Youtube", extension = "mp4"):

		yt = YT(link)
		yt_stream = YT.streams.filter(progressive = True, file_extension = extension).order_by("resoluiton").desc().first()
		yt_stream.download(output_path = save_path, filename = save_name)

		return


	def __get_link(self):
		link = self.link_entry.get()
		path = self.path_entry.get()
		name = self.name_entry.get()
		ext = self.ext_entry.get()
		self.__downloader(link, path, name, ext)

		return


	def run_app(self):
		self.window.mainloop()
		return


if __name__=="__main__":
	app = YouTubeDownloader()
	app.run_app()