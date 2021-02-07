# try:
#     with open(r"E:\\temp\testowy*.txt", 'a+') as file:
#         file.writelines("SUCCES\n")
# except OSError as e:
#     print('Error opening file', e)
import time
class TimeMeasure:
    def __init__(self):
        pass

    def __enter__(self):  # metodę enter trzeba zdefiniować,
        # jezeli klasa ma być uzywana jako cpontaxt manager
        print("entering...")
        self.__start = time.time()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('exiting.....')
        self.__stop = time.time()
        self.difference = self.__stop - self.__start
        print(f"Execution time: {self.difference}")

with TimeMeasure():
    for i in range(5):
        print(i ** 5)
        time.sleep(1)

#########################   LAB      #######################

class HtmlCM:
    def __init__(self):
        pass
    def __enter__(self):
        print("""
<TABLE>
<TR>
    <TH>Number</TH><TH>Description</TH>
</TR> """)

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("</TABLE>")

with HtmlCM():
    print("""<TR>
     <TD>1</TD><TD>Say hello!</TD)
</TR>
<TR>
     <TD>2</TD><TD>Say good bye!</TD)
</TR> """)