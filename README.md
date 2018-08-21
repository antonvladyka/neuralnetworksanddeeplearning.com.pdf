# Neural Networks and Deep Learning
## by Michael Nielsen
This is an attempt to convert [online version](http://neuralnetworksanddeeplearning.com) of Michael Nielsen's book 'Neural Networks and Deep Learning' into LaTeX source.

### Current status
1. Chapter 1: done
2. Chapter 2: done
3. Chapter 3: done
4. Chapter 4: includes a lot of interactive JS-based elements. In progress. By now, interactive elements are replaced with intuitive (I hope) graphs, but text is not fully adapted.
5. Chapter 5: done
6. Chapter 6: done

I observed some missed Python code in the online version of network3.py:
```print('The corresponding test accuracy is {0:.2
   test_accuracy))
   ...
   print("Best validation accuracy of {0:.2
      best_validation_accuracy, best_iteration))
   ...
   print("Corresponding test accuracy of {0:.2
 ```
So, these parts were replaced with the correct ones from the source code repo.

Can be compiled into any desired format, using XeLaTeX — with any desired font.

As a general design, I used my PhD thesis style: 17x24 cm paper, 9pt font, Charter/Mathdesign, own designed charper titles, chapter labels etc.

Typography adjusted (- → –, "" → “ ”)

Bibliography — maybe to collect all cited research papers?

