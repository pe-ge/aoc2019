input_signal = "59708372326282850478374632294363143285591907230244898069506559289353324363446827480040836943068215774680673708005813752468017892971245448103168634442773462686566173338029941559688604621181240586891859988614902179556407022792661948523370366667688937217081165148397649462617248164167011250975576380324668693910824497627133242485090976104918375531998433324622853428842410855024093891994449937031688743195134239353469076295752542683739823044981442437538627404276327027998857400463920633633578266795454389967583600019852126383407785643022367809199144154166725123539386550399024919155708875622641704428963905767166129198009532884347151391845112189952083025"
offset = 5970837

input_signal = input_signal * 10000
input_signal = list(map(int, input_signal))
input_signal = input_signal[offset:]

for _ in range(100):
    last = 0
    for idx in range(len(input_signal) - 1, -1, -1):
        input_signal[idx] = (input_signal[idx] + last) % 10
        last = input_signal[idx]

print(''.join(map(str, input_signal[:8])))