#  from http://www.checkio.org/mission/count-neighbours/  



def count_neighbours(neighbourhood, yval, xval):
    dimension = len(neighbourhood)
    xvals = []
    yvals = []
    neighbors =[]
    if not(yval==0):
        yvals.append(yval-1)
    yvals.append(yval)
    if not(yval==dimension-1):
        yvals.append(yval+1)
    if not(xval==0):
        xvals.append(xval-1)
    xvals.append(xval)
    if not(xval==dimension-1):
        xvals.append(xval+1)
    for eachx in xvals:
        for eachy in yvals:
            if ((neighbourhood[eachx][eachy] == 1) and not((xval,yval)==(eachx,eachy))):
                neighbors.append((eachx,eachy))
    return len(neighbors)


