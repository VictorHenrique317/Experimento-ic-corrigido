from base.file_system import FileSystem
from models.pattern import Pattern


class Quality():

    @staticmethod
    def __findMostSimilarFoundPattern(planted_pattern, found_patterns):
        # returns the most similar found pattern to a given planted one
        similarities = []
        for found_pattern in found_patterns:
            jaccard_index = found_pattern.jaccardIndex(planted_pattern)
            similarities.append(jaccard_index)

        most_similar_index = similarities.index(max(similarities))
        most_similar_pattern = found_patterns[most_similar_index]
        return most_similar_pattern

    @staticmethod
    def __multiplePatternUnion(patterns):
        dimension = patterns[0].getDimension()
        union = Pattern("", dimension)
        for pattern in patterns:
            union = union.union(pattern)
        return union

    @staticmethod
    def __multiplePatternUnionArea(patterns):
        return Quality.__multiplePatternUnion(patterns).area()

    @staticmethod
    def calculate(found_patterns, planted_patterns):
        all_p_intersection_argmax = []
        
        if len(found_patterns) == 0: # no patterns found by the algorithm
            return 0 # zero quality
        
        for planted_pattern in planted_patterns:
            most_similar_found = Quality.__findMostSimilarFoundPattern(planted_pattern, found_patterns)

            p_intersection_argmax = most_similar_found.intersection(planted_pattern)
            all_p_intersection_argmax.append(p_intersection_argmax)
        
        numerator = Quality.__multiplePatternUnionArea(all_p_intersection_argmax)
        
        planted_patterns_union = Quality.__multiplePatternUnion(planted_patterns)
        found_patterns_union = Quality.__multiplePatternUnion(found_patterns)

        denominator = planted_patterns_union.unionArea(found_patterns_union)
        return numerator / denominator
        

