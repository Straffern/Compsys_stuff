from dataclasses import dataclass


@dataclass(frozen=True)
class Translation:
    __slots__ = ['VPN', 'TLBI', 'TLBT', 'binary_address']
    VPN: int
    TLBI: int
    TLBT: int
    binary_address: str

@dataclass(frozen=True)
class MMU:
    """MMU - Used to translate virtual address to physical address.

        Args:
            n (int): Virtual address width in bits. Virtual address space is: N=2^n
            P (str): Size in bytes. eg. 500 (bytes), 1.3kb or 47gb
            T (int): TLB sets
    """
    __slots__ = ['n', 'P', 'T']
    n: int
    P: str
    T: int

    @staticmethod
    def __toBytes(byteSize: str) -> int:
        import re

        _bytesize = byteSize.lower()
        regexString = r'^(?=.)([0-9]*(\.([0-9]+)(kb|mb|gb){1}$)?)(\d+(kb|mb|gb))?$'
        isByteString = re.match(regexString, byteSize)#, re.I)
        assert(isByteString) # Asserts that the passed string matches the correct form.

        result:int = 0
        if 'kb' in _bytesize:
            result = float(_bytesize[:-2]) * float(2**10)
        if 'mb' in _bytesize:
            result = float(_bytesize[:-2]) * float(2**20)
        if 'gb' in _bytesize:
            result = float(_bytesize[:-2]) * float(2**30)
        else:
            return int(byteSize)
        return int(result)
    def __toBinary(self, number: int, n=None) -> str:
        _n = n if n!=None else self.n
        return format(number, f'#0{_n+2}b')
    def translate(self, virtual_address: str) -> Translation:
        from math import log
        bin_virtual_address: str = self.__toBinary(int(virtual_address, 16))
        p: int = int(log(self.__toBytes(self.P), 2))
        t: int = int(log(self.T, 2))
        VPN: int = int(bin_virtual_address[:-p], 2)
        bin_vpn = self.__toBinary(VPN, self.n-p)

        TLBI: int = int(bin_vpn[-t:], 2)
        TLBT: int = int(bin_vpn[:-t], 2)

        return Translation(VPN=VPN, TLBI=TLBI, TLBT=TLBT, binary_address=bin_virtual_address)

