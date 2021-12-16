with open('sample_input.txt', 'r') as f:
    packets = f.read().splitlines()

packet_list = []


class Packet():

    def __init__(self, packet: str):
        self.packet = packet
        self.cursor = 0
        self.total_parsed = 0


    def retrieve_bits(self, amount: int):
        assert amount > -1

        rtn = self.packet[self.cursor:self.cursor+amount]
        self.cursor += amount

        self.total_parsed += amount

        return rtn

    
    def set_cursor_by_offset(self, offset: int) -> None:
        self.cursor += offset

        self.total_parsed += offset



    def set_literal_val(self, val: int) -> None:

        assert self.type == 'literal'

        self.literal_val = val
    


    def set_version(self, version: int) -> None:
        self.version = version



    def set_type_id(self, type_id: int) -> None:
        self.type_id = type_id

        match self.type_id:

            case 4:
                print('set to literal')
                self.type = 'literal'

            case _:
                self.type = 'operator'



def parse_packet(packet: Packet) -> bin:
    '''
    Parse 1 packet and return the rest
    of the packets without the packet that
    was just parsed
    '''

    
    version = int(packet.retrieve_bits(3), 2)
    type_id = int(packet.retrieve_bits(3), 2)

    # packet.total_parsed += 6

    packet.set_version(version)
    packet.set_type_id(type_id)


    match packet.type:

        case 'literal':

            literal_str = str()

            while True:
                
                bits = packet.retrieve_bits(5)
                # packet.total_parsed += 5
                print(f'bits: {bits}')
                
                if bits[0] == '0':
                    
                    literal_str += str(bits)[1:]
                    break

                elif bits[0] == '1':
                    literal_str += str(bits)[1:]

            packet.set_literal_val(int(literal_str, 2))

            if packet.total_parsed % 4 != 0:
                packet.set_cursor_by_offset(packet.total_parsed % 4)
            
            # print(packet.literal_val)


        case 'operator':
            length = packet.retrieve_bits(1)

            match length:

                case '0':
                    length_sub_packets = packet.retrieve_bits(15)


                case '1':
                    num_sub_packets = packet.retrieve_bits(11)
            


if __name__ == '__main__':


    initial_packet = packets[0]
    bin_packet = bin(int(initial_packet, 16))[2:]

    packet_list.append(Packet(bin_packet))

    parse_packet(packet_list[0])