PAYLOAD='''
    def _composed_layout_features(self, features: AnomalyFeatures):
        """Review one well-supported repeat outside an exact source title.

        A repeated key can destroy Thai-language evidence in an otherwise
        wrong-layout span. Names are removed from scoring evidence only;
        neither the input nor a corrected candidate is sent to answering.
        """
        if features.layout_score >= self.layout_threshold or features.repeat_score < self.repeat_threshold or not features.repeat_spans:
            return features, None
        repeat = features.repeat_spans[0]
        if (repeat.run_length != 2 or repeat.interpretation != 'accidental_candidate'
                or repeat.original_seen or not repeat.candidate_seen
                or repeat.candidate_quality - repeat.original_quality < 0.15):
            return features, None
        from app.core.locale import _catalog_title_pattern
        pattern = _catalog_title_pattern()
        names = list(pattern.finditer(features.input_text)) if pattern else []
        if not names or any(repeat.start < name.end() and name.start() < repeat.end for name in names):
            return features, None
        residual = pattern.sub(' ', repeat.candidate_span)
        if len(residual.strip()) < 5:
            return features, None
        candidate = self.detector.analyze(residual)
        if candidate.layout_direction != 'thai_intended_english_active' or candidate.layout_score < max(0.65, self.layout_threshold):
            return features, None
        evidence = {'method':'exact_catalog_title_and_single_accidental_repeat',
                    'original_layout_score':features.layout_score,
                    'rescored_layout_score':candidate.layout_score,
                    'scoring_residual':residual,
                    'repeat_span':[repeat.start,repeat.end],
                    'protected_title_spans':[[n.start(),n.end()] for n in names],
                    'rescored_spans':[vars(span) for span in candidate.layout_spans],
                    'raw_input_mutated':False,'candidate_used_as_answer_input':False}
        # Retain raw input and its original span offsets. Composed span
        # offsets refer to the explicitly logged residual, not the raw text.
        return replace(features,layout_score=candidate.layout_score,
                       layout_direction=candidate.layout_direction,
                       layout_reason='composed repeat/layout review: '+candidate.layout_reason), evidence

'''
