from pyrosim.commonFunctions import Save_Whitespace

class CONTACT_URDF:

    def __init__(self,friction):

        self.depth = 3

        self.string1 = "<contact>"

        self.string2 = '    <lateral_friction value="' + str(friction[0]) + '"/>'

        self.string3 = '    <rolling_friction value="' + str(friction[1]) + '"/>'

        self.string4 = '    <spinning_friction value="' + str(friction[2]) + '"/>'

        self.string5 = "</contact>"

    def Save(self,f):

        Save_Whitespace(self.depth,f)

        f.write( self.string1 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string2 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string3 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string4 + '\n' )

        Save_Whitespace(self.depth,f)

        f.write( self.string5 + '\n' )
