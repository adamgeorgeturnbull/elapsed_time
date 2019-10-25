library(readr)
library(tidyr)
library(ggplot2)
library(Hmisc)
library(plyr)
library(RColorBrewer)
library(reshape2)
library(dplyr)

ub <- function(x) mean(x) + sd(x)
lb <- function(x) mean(x) - sd(x)
my_data <- read.csv(file="*insert path*/elapsed_time_09_09.csv", header=TRUE, sep=",")
my_datal <- melt(my_data, id.vars = c("ID"), measure.vars = c("Gradient3Offtask", "Gradient3NTET", "Gradient3NTETneg", "Gradient3Ontask"), variable.name = "Gradient", value.name = "GradientScore")
sumld<- ddply(my_datal, ~Gradient, summarise, mean = mean(GradientScore), median = median(GradientScore), lower = lb(GradientScore), upper = ub(GradientScore))
g <- ggplot(data = my_datal, aes(y = GradientScore, x = Gradient, fill = Gradient)) +
  geom_flat_violin(position = position_nudge(x = .2, y = 0), alpha = .8) +
  geom_point(aes(y = GradientScore, color = Gradient), position = position_jitter(width = .15), size = .5, alpha = 0.8) +
  geom_boxplot(width = .1, guides = FALSE, outlier.shape = NA, alpha = 0.5) +
  expand_limits(x = 5.25, y = c(-0.6,0.6)) +
  guides(fill = FALSE) +
  guides(color = FALSE) +
  scale_color_brewer(palette = "Spectral") +
  scale_fill_brewer(palette = "Spectral") +
  coord_flip() +
  theme_bw() +
  raincloud_theme
g
