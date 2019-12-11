def formater(code):
    z= code.strip().split("\n")
    code=""   
    for j in z:
        if j.strip().startswith("!"):
            code+=j +"\n"
        else:
            code+=formaterNext(j)
    return code

def formaterNext(line):
    nbmax=70
    tab=" "
    code=""
    s=0
    ff = len(line)-len(line.lstrip())
    line = line.strip()
    h=""
    if len(line)<=nbmax or line[-1]=="&":
        code+=tab*ff+line
    while len(line)>nbmax and line[-1]!="&" :
        
        nb=nbmax
        z = ff+8 if s>0 else ff
        while (line[nb-1]!=" ") and nb>1:
            nb = nb-1
        if nb>1:
            h+=tab*z+line[0:nb]+" &\n"
            line=(line[nb:]).strip()
            if len(line)<=nbmax:
                h+=tab*(ff+8)+line
                break
        else:
            h += tab*z+line
            break
        s=s+1
        
    code+=h+"\n"
    
    return code