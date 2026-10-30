from pyrosim.commonFunctions import Save_Whitespace

class GEOMETRY_URDF: 

    def __init__(self,type,size):

        self.depth   = 3

        self.string1 = '<geometry>'

        if type == "cube":

            sizeString = str(size[0]) + " " + str(size[1]) + " " + str(size[2])

            self.string2 = '    <box size="' + sizeString + '" />'

        elif type == "cylinder":

            self.string2 = '    <cylinder radius="' + str(size[0]) + '" length="' + str(size[1]) + '" />'

        self.string3 = '</geometry>'

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )
