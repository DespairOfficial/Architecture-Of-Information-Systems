format PE console

entry Start

include 'win32a.inc'

section '.data' data readable writeable
        formatA db '%d', 0
        formatB db '%d', 0
        formatC db '%d', 0

        ia db 'input A: ', 0
        ib db 'input B: ', 0
        ic db 'input C: ', 0

        resultStr db 'z=%d',0
        emptyStr db '%d', 0
        point db ',', 0

        A rd 1
        B rd 1
        C rd 1
        D dd ?
        F dd ?

        NULL = 0

section '.code' code readable executable


        Start:
                push ia
                call [printf]

                push A
                push formatA
                call [scanf]

                push ib
                call [printf]

                push B
                push formatB
                call [scanf]

                push ic
                call [printf]

                push C
                push formatC

                call [scanf]

                mov eax, [A]
                add eax, [B]
                imul eax, [C]
                sub eax, 24

                mov ebx, [A]
                imul ebx, [C]
                sub ebx, 1
                mov [F], ebx

                mov ecx, ebx
                mov edx, 0
                div ecx
                mov [D], edx

                push eax
                push resultStr
                call [printf]

                push point
                call [printf]

                mov ebx, 0
                lp:
                        mov eax, [D]
                        mov ecx, [F]
                        imul eax, 10

                        mov edx, 0
                        div ecx
                        mov [D], edx

                        push eax
                        push emptyStr
                        call [printf]

                        add ebx, 1
                        cmp ebx, 8
                  jne lp

                call [getch]
                push NULL
                call [ExitProcess]

section 'idata' import data readable
        library kernel, 'kernel32.dll',\
                msvcrt, 'msvcrt.dll'

        import kernel,\
               ExitProcess, 'ExitProcess'

        import msvcrt,\
               printf, 'printf',\
               getch, '_getch',\
               scanf, 'scanf'

