xml_escape_table = {
    "&": "&amp;",
     '"': "&quot;",
     "'": "&apos;",
     ">": "&gt;",
     "<": "&lt;",
     }

def xml_escape(text):
    return "".join(xml_escape_table.get(c, c) for c in text)





'''f=open("Jenkinsfile")
lines=f.read()
print lines
print xml_escape(lines)'''