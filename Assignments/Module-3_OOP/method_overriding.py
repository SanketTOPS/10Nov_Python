class master:
    def header(self,hpage):
        print(f"This is {hpage}.")
    
    def footer(self,fpage):
        print(f"This is {fpage}.")

class home(master):
    def header(self, hpage):
        return super().header(hpage)
    def footer(self, fpage):
        return super().footer(fpage)
    
class about(master):
    def header(self, hpage):
        return super().header(hpage)
    def footer(self, fpage):
        return super().footer(fpage)