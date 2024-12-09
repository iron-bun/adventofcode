#!/usr/bin/env python3

with open("day09.txt") as f:
  data = list(map(int,list(f.readline().strip())))

  disk_size = sum(map(int, data))
  data_idx = 0
  file_idx = 0
  file_id = 0
  max_file_id = (len(data) + 1)//2 - 1
  file = True

  checksum = 0
  while file_id <= max_file_id:
    if file:
      tmp_file_id = file_id
      tmp_start = file_idx
      tmp_length = data[data_idx]

      file_id += 1
      file_idx += data[data_idx]
      file = not file
      data_idx += 1

    elif data[-1] > data[data_idx]:
      tmp_file_id = max_file_id
      tmp_start = file_idx
      tmp_length = data[data_idx]

      data[-1] -= data[data_idx]
      file_idx += data[data_idx]
      file = not file
      data_idx += 1

    elif data[-1] == data[data_idx]:
      tmp_file_id = max_file_id
      tmp_start = file_idx
      tmp_length = data[data_idx]

      del data[-1]
      del data[-1]
      file_idx += data[data_idx]
      max_file_id -= 1
      file = not file
      data_idx += 1
    else: #data[-1] < data[data_idx]:
      tmp_file_id = max_file_id
      tmp_start = file_idx
      tmp_length = data[-1]

      del data[-1]
      del data[-1]
      max_file_id -= 1
      data[data_idx] -= tmp_length
      file_idx += tmp_length

    tmp_checksum = tmp_file_id * (tmp_start + tmp_length-1) * (tmp_start + tmp_length) / 2 - tmp_file_id * tmp_start * (tmp_start-1) / 2
    checksum += int(tmp_checksum)

  print(checksum)

with open("day09.txt") as f:
  data = list(map(int,list(f.readline().strip())))
  data += [0]

  file_idx = 0
  file_id = 0
  disc = {}
  for k in range(0,len(data),2):
    disc[file_idx] = [file_id, data[k], data[k+1]]
    file_idx += data[k] + data[k+1]
    file_id += 1

  rkeys = sorted(disc.keys(), reverse=True)

  for idx in range(len(rkeys)):
    tmp_file = disc[rkeys[idx]]

    for k in sorted(disc.keys()):
      if k >= rkeys[idx]:
        break

      if disc[k][2] >= tmp_file[1]:
        tmp_file[2] = disc[k][2] - tmp_file[1]
        disc[k][2] = 0

        disc[k+disc[k][1]] = tmp_file
        disc[rkeys[idx+1]][2] += tmp_file[1] + tmp_file[2]

        del disc[rkeys[idx]]
        break

  checksum = 0
  for k in sorted(disc.keys()):
    tmp_file = disc[k]
    tmp_checksum = tmp_file[0] * (k + tmp_file[1]-1) * (k + tmp_file[1]) / 2 - tmp_file[0] * k * (k-1) / 2
    checksum += int(tmp_checksum)
  print(checksum)
