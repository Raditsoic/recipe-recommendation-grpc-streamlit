# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recipe_recommendation.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x1brecipe_recommendation.proto\x12\x18RecipeRecommendationGRPC\"G\n\x06Recipe\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05title\x18\x02 \x01(\t\x12\x13\n\x0bingredients\x18\x03 \x01(\t\x12\r\n\x05steps\x18\x04 \x01(\t\"\x16\n\x14GetAllRecipesRequest\"J\n\x15GetAllRecipesResponse\x12\x31\n\x07recipes\x18\x01 \x03(\x0b\x32 .RecipeRecommendationGRPC.Recipe\"G\n\x13\x43reateRecipeRequest\x12\x30\n\x06recipe\x18\x01 \x01(\x0b\x32 .RecipeRecommendationGRPC.Recipe\"H\n\x14\x43reateRecipeResponse\x12\x30\n\x06recipe\x18\x01 \x01(\x0b\x32 .RecipeRecommendationGRPC.Recipe\"S\n\x13UpdateRecipeRequest\x12\n\n\x02id\x18\x01 \x01(\t\x12\x30\n\x06recipe\x18\x02 \x01(\x0b\x32 .RecipeRecommendationGRPC.Recipe\"H\n\x14UpdateRecipeResponse\x12\x30\n\x06recipe\x18\x01 \x01(\x0b\x32 .RecipeRecommendationGRPC.Recipe\"!\n\x13\x44\x65leteRecipeRequest\x12\n\n\x02id\x18\x01 \x01(\t\"\'\n\x14\x44\x65leteRecipeResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xd5\x03\n\x14RecipeRecommendation\x12p\n\rGetAllRecipes\x12..RecipeRecommendationGRPC.GetAllRecipesRequest\x1a/.RecipeRecommendationGRPC.GetAllRecipesResponse\x12m\n\x0cUpdateRecipe\x12-.RecipeRecommendationGRPC.UpdateRecipeRequest\x1a..RecipeRecommendationGRPC.UpdateRecipeResponse\x12m\n\x0c\x44\x65leteRecipe\x12-.RecipeRecommendationGRPC.DeleteRecipeRequest\x1a..RecipeRecommendationGRPC.DeleteRecipeResponse\x12m\n\x0c\x43reateRecipe\x12-.RecipeRecommendationGRPC.CreateRecipeRequest\x1a..RecipeRecommendationGRPC.CreateRecipeResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recipe_recommendation_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_RECIPE']._serialized_start=57
  _globals['_RECIPE']._serialized_end=128
  _globals['_GETALLRECIPESREQUEST']._serialized_start=130
  _globals['_GETALLRECIPESREQUEST']._serialized_end=152
  _globals['_GETALLRECIPESRESPONSE']._serialized_start=154
  _globals['_GETALLRECIPESRESPONSE']._serialized_end=228
  _globals['_CREATERECIPEREQUEST']._serialized_start=230
  _globals['_CREATERECIPEREQUEST']._serialized_end=301
  _globals['_CREATERECIPERESPONSE']._serialized_start=303
  _globals['_CREATERECIPERESPONSE']._serialized_end=375
  _globals['_UPDATERECIPEREQUEST']._serialized_start=377
  _globals['_UPDATERECIPEREQUEST']._serialized_end=460
  _globals['_UPDATERECIPERESPONSE']._serialized_start=462
  _globals['_UPDATERECIPERESPONSE']._serialized_end=534
  _globals['_DELETERECIPEREQUEST']._serialized_start=536
  _globals['_DELETERECIPEREQUEST']._serialized_end=569
  _globals['_DELETERECIPERESPONSE']._serialized_start=571
  _globals['_DELETERECIPERESPONSE']._serialized_end=610
  _globals['_RECIPERECOMMENDATION']._serialized_start=613
  _globals['_RECIPERECOMMENDATION']._serialized_end=1082
# @@protoc_insertion_point(module_scope)
