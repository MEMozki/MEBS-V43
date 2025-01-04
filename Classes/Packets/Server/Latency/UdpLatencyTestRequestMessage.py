from Classes.Packets.PiranhaMessage import PiranhaMessage


class UdpLatencyTestRequestMessage(PiranhaMessage):
    def __init__(self, messageData):
        super().__init__(messageData)
        self.messageVersion = 0
    def decode(self):
    	self.readVInt()
    	self.readVInt()
    	self.readBytesLength()
    	self.readBytes()
    def encode(self):
    	self.writeVInt(0)
    	self.writeVInt(0)
    	self.writeBytesLength(0)
    	self.writeBytes(0)
    	return {}
        
    def execute(message, calling_instance, fields):
        pass

    def getMessageType(self):
        return 19002

    def getMessageVersion(self):
        return self.messageVersion
