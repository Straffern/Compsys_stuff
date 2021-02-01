import re
import sys, getopt
from mmu import *
from prettyprint import print_binary


def main(argv):
    n: int = 0
    P: str = ''
    T: int = 0
    VA: str = ''

    try:
        opts, args = getopt.getopt(argv, "hn:P:T:i:", ["vWidth=", "pSize=", "tlbSets=", "vAddress="])
        if opts == []:
            raise getopt.GetoptError("No arguments")
    except getopt.GetoptError:
        print ('mmu.py -n <Virtual Address Width> -P <Page Size> -T <TLB sets> -i <Virtual Adress>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('mmu.py -n <Virtual Address Width> -P <Page Size> -T <TLB sets> -i <Virtual Adress>')
            sys.exit()
        elif opt in ('-n', '--vWidth'):
            assert(int(arg) > 4)
            n = int(arg)
        elif opt in ('-P', '--pSize'):
            isByteSize = re.match(r'^(?=.)([0-9]*(\.([0-9]+)(kb|mb|gb){1}$)?)(\d+(kb|mb|gb))?$', arg)
            assert(isByteSize)
            P = arg
        elif opt in ('-T', '--tlbSets'):
            assert(int(arg) > 1)
            T = int(arg)
        elif opt in ('-i', '--vAddress'):
            assert(int(arg, 16) > 0)
            VA = arg

    print (f'Virtual address width is: {n:>15}')
    print (f'Page size is: {P:>15}')
    print (f'Number of TLB sets: {T:>15}')
    print (f'Virtual Address is: {VA:>15}')

    mmu = MMU(n, P, T)
    translation = mmu.translate(VA)

    print(f'{"":>20}<<<<<{"Bits for Virtual Address":^10}>>>>>{"":<20}\n')
    print_binary(width=n, address=translation.binary_address)
    print()

    print(f'{"":>20}<<<<<{"Remaining stuff:":^10}>>>>>{"":<20}\n')
    print(f'{"Virtual Page Number (VPN):":>20}{translation.VPN:>10}')
    print(f'{"Translation Lookup Buffer Index (TLBI):":>20}{translation.TLBI:>10}')
    print(f'{"Translation Lookup Buffer Tag (TLBT):":>20}{translation.TLBT:>10}') 


if __name__ == "__main__":
    # print(sys.argv)
    main(sys.argv[1:])
