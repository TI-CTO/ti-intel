-- Fix "Function Search Path Mutable" warnings by setting search_path.

ALTER FUNCTION public.search_intel_semantic SET search_path = '';
ALTER FUNCTION public.intel_items_search_text_trigger SET search_path = '';
