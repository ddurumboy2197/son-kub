# test_kub.py
import pytest
from kub import kub

def test_kub():
    assert kub(1) == 1
    assert kub(2) == 8
    assert kub(3) == 27
    assert kub(4) == 64
    assert kub(5) == 125

def test_kub_negative():
    with pytest.raises(ValueError):
        kub(-1)

def test_kub_zero():
    with pytest.raises(ValueError):
        kub(0)

def test_kub_large():
    assert kub(100) == 1000000000
```

```javascript
// kub.test.js
import { kub } from './kub';

describe('kub', () => {
  it('should return the cube of a number', () => {
    expect(kub(1)).toBe(1);
    expect(kub(2)).toBe(8);
    expect(kub(3)).toBe(27);
    expect(kub(4)).toBe(64);
    expect(kub(5)).toBe(125);
  });

  it('should throw an error for negative numbers', () => {
    expect(() => kub(-1)).toThrowError();
  });

  it('should throw an error for zero', () => {
    expect(() => kub(0)).toThrowError();
  });

  it('should return the cube of a large number', () => {
    expect(kub(100)).toBe(1000000000);
  });
});
