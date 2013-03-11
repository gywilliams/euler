primes = [2]

def isPrime(x):
  maxPrimeToCheck = pow(x, .5)
  for prime in primes:
    if prime > maxPrimeToCheck:
      return True
    if x % prime == 0:
      return False
  return True

def findNextPrime():
  currentNumber = primes[-1] + 1
  while not isPrime(currentNumber):
    currentNumber += 1
  primes.append(currentNumber)

def findNthPrime(n):
  while len(primes) < n:
    findNextPrime()
  return primes[n - 1]

print '1st prime: ', findNthPrime(1)
print '10th prime: ', findNthPrime(10)
print '10001th prime: ', findNthPrime(10001)
