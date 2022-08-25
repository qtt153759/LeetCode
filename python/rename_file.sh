for x in *py; do
  mv -- "$x" "${x//_/}"
done