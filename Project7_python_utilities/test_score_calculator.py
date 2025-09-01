import tkinter
import tkinter.messagebox

class GUI:

   def __init__(self):
       self.main_window = tkinter.Tk()

       self.tf1 = tkinter.Frame(self.main_window)
       self.tf2 = tkinter.Frame(self.main_window)
       self.mf = tkinter.Frame(self.main_window)
       self.bf = tkinter.Frame(self.main_window)

       self.label1 = tkinter.Label(self.tf1, text='Enter test score1:')
       self.test1 = tkinter.Entry(self.tf1, width=10)
       self.label2 = tkinter.Label(self.tf2, text='Enter test score2:')
       self.test2 = tkinter.Entry(self.tf2, width=10)
       self.result_label = tkinter.Label(self.mf, text='Average score:')
       self.avg_val = tkinter.StringVar()
       self.average_label = tkinter.Label(self.mf, textvariable=self.avg_val)

       self.avg = tkinter.Button(self.bf, text='Average', command=self.cal_avg)
       self.quit = tkinter.Button(self.bf, text='Quit', command=self.main_window.destroy)

       self.label1.pack(side='left')
       self.test1.pack(side='left')
       self.label2.pack(side='left')
       self.test2.pack(side='left')
       self.result_label.pack(side='left')
       self.average_label.pack(side='left')

       self.avg.pack(side='left')
       self.quit.pack(side='left')

       self.tf1.pack()
       self.tf2.pack()
       self.mf.pack()
       self.bf.pack()

       tkinter.mainloop()

   def cal_avg(self):
       s1 = float(self.test1.get())
       s2 = float(self.test2.get())
       average = (s1 + s2) / 2
       self.avg_val.set(average)

test_scores = GUI()