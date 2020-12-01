# https://adventofcode.com/2020/day/1

library(tidyverse)

input = read_delim("01-input.txt", delim = "\n", col_names = "value")

# Part 1

part_1 = input %>% 
  mutate(diff_2020 = 2020 - value,
         in_row = diff_2020 %in% value)

part_1 %>% 
  filter(in_row) %>% 
  select(value) %>% 
  prod()

# Part 2

part_2 = c(input$value)

part_2_df = expand.grid(part_2, part_2, part_2) %>% 
  mutate(total = Var1 + Var2 + Var3) %>% 
  filter(total == 2020) %>% 
  mutate(prod = Var1 * Var2 * Var3)

