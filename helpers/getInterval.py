

def getInterval(expression) -> list:
    [start, end] = expression.split("-")

    if start > end:
        startInterval = end
        endInterval = start

    startInterval = start
    endInterval = end

    ports = []

    for port in range(int(startInterval), int(endInterval)):
        ports.append(port)

    return ports
