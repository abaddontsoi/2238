class nodes():
    def __init__(self, stationName):
        self.routing_table = {}
        self.station_name = stationName

    def __repr__(self):
        return self.station_name 

    def interfaceIsFree(self, interface=None):
        print(f"{self} is checking interface {interface} is free....")
        if self.routing_table.get(interface):
            print(f'interface {interface} is busy\n')
        else:
            print(f'interface {interface} is free\n')
        return self.routing_table.get(interface) is None

    def connectTo(self, self_interface: str, target, target_interface: str, delay=0):
        if self.interfaceIsFree(self_interface) and target.interfaceIsFree(target_interface):
            self.routing_table.update({
                self_interface: {
                    "Node": target,
                    "interface": target_interface,
                    "delay":delay,
                }
            })
            target.receiveConnection(target_interface, self, self_interface, delay)

    # deprecated 
    def receiveConnection(self, self_interface: str, target, target_interface: str, delay=0):
        if self.interfaceIsFree(self_interface):
            self.routing_table.update({
                self_interface: {
                    "Node": target,
                    "interface": target_interface,
                    "delay": delay,
                }
            })