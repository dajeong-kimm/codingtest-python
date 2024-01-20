# 문자열 배열을 받아서 애너그램 단위로 그룹핑

from ast import List
import collections


def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagrams = collections.defaultdict(list)

    for word in strs:
        #현재 단어를 정렬한 후, 정렬된 문자열을 키로 사용
        anagrams[''.join(sorted(word))].append(word)

    
    return list(anagrams.value())