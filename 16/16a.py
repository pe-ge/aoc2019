input_signal = "59708372326282850478374632294363143285591907230244898069506559289353324363446827480040836943068215774680673708005813752468017892971245448103168634442773462686566173338029941559688604621181240586891859988614902179556407022792661948523370366667688937217081165148397649462617248164167011250975576380324668693910824497627133242485090976104918375531998433324622853428842410855024093891994449937031688743195134239353469076295752542683739823044981442437538627404276327027998857400463920633633578266795454389967583600019852126383407785643022367809199144154166725123539386550399024919155708875622641704428963905767166129198009532884347151391845112189952083025"
input_signal = list(map(int, input_signal))

def generate_pattern(order):
    pattern = []
    for _ in range(order):
        pattern.append(0)
    for _ in range(order):
        pattern.append(1)
    for _ in range(order):
        pattern.append(0)
    for _ in range(order):
        pattern.append(-1)

    pattern.append(pattern[0])
    return pattern[1:]

def apply_fft(signal, patterns):
    result = [0] * len(signal)
    for order, pattern in enumerate(patterns):
        for idx, signal_val in enumerate(signal):
            result[order] += signal_val * pattern[idx % len(pattern)]
        result[order] = abs(result[order]) % 10

    return result

patterns = [generate_pattern(order) for order in range(1, len(input_signal)+1)]
for _ in range(100):
    input_signal = apply_fft(input_signal, patterns)

print(''.join(map(str, input_signal[:8])))
