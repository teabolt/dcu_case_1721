echo "[UNIT TESTS]"
python3 -m unittest tests/test_*

echo "[MAKE TESTS]"
make test
