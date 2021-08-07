'''
template <class ForwardIterator, class T>
  ForwardIterator lower_bound (ForwardIterator first, ForwardIterator last, const T& val)
{
  ForwardIterator it;
  iterator_traits<ForwardIterator>::difference_type count, step;
  count = distance(first,last);
  while (count>0)
  {
    it = first; step=count/2; advance (it,step);
    if (*it<val) {                 // or: if (comp(*it,val)), for version (2)
      first=++it;
      count-=step+1;
    }
    else count=step;
  }
  return first;
}
'''
from pystl import is_sorted
def lower_bound(self_list, val):
    if is_sorted.is_sorted(self_list) == False:
      raise ValueError("Unsorted: The list should be sorted")
    first = 0
    last = len(self_list) - 1
    count = last - first + 1
    if val<self_list[first]:
      return -1
    if val>self_list[last]:
      return last+1
    while(count>0):
        it = first
        step = (int)(count/2)
        it = it+step
        print(it)
        if(self_list[it] < val):
            first= 1+it
            count = count - step + 1
        else:
            count = step
    return first
'''
@Fix the range queries
def lower_bound(self_list, first, last, val):
    count = last - first + 1
    print(first, last, val)
    while(count>0):
        it = first
        step = (int)(count/2)
        it = it+step
        print(it)
        if(self_list[it] < val):
            first= 1+it
            count = count - step + 1
        else:
            count = step
    return first

list = [10, 10, 10, 20, 20, 20, 30, 30]
print(lower_bound(list,3,7,30)) 
'''
