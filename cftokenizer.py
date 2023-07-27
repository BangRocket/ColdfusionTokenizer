import re

class CFToken:

  def __init__(self, value, line, col):
    self.value = value
    self.line = line 
    self.col = col

  def __repr__(self):
    return f'{self.__class__.__name__}(value={self.value!r}, line={self.line}, col={self.col})'

class CFTagToken(CFToken):
  
  TAG_REGEX = re.compile(r'<\/?\w.*?>')

  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    self.name = value[1:-1] 

class CFStringToken(CFToken):

  STRING_REGEX = re.compile(r'(".*?")|(\'.*?\')')
  LITERAL = 'literal'
  SINGLE_QUOTE = 'single quote'

  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    self.type = self.LITERAL if value.startswith('"') else self.SINGLE_QUOTE

class CFOperatorToken(CFToken):

  OPERATORS = {'=': 'ASSIGN', '==': 'EQ', '!=': 'NEQ', 
               '<': 'LT', '>': 'GT', '<=': 'LTE', '>=': 'GTE',
               '&&': 'AND', '||': 'OR', '+': 'ADD', '-': 'SUB',
               '*': 'MUL', '/': 'DIV'}

  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    self.type = self.OPERATORS.get(value, 'UNKNOWN')

class CFKeywordToken(CFToken):
  
  KEYWORDS = {    
    'if': 'if',
    'else': 'else',
    'while': 'while',
    'for': 'for',
    'function': 'function',
    'component': 'component',
    'property': 'property',
    'return': 'return',
    'include': 'include',
    'import': 'import',
    'param': 'param',
    'try': 'try',
    'catch': 'catch',
    'interface': 'interface',
    'implements': 'implements'
    }

  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    self.keyword = self.KEYWORDS.get(value)
  
  def __str__(self):
    return f'CFKeywordToken({self.keyword})' if self.keyword else 'CFKeywordToken(UNKNOWN)'
    
class CFFunctionToken(CFToken):

  FUNCTIONS = {
    'Abs': 'Abs',
    'ACos': 'ACos',
    'AddSOAPRequestHeader': 'AddSOAPRequestHeader',
    'AddSOAPResponseHeader': 'AddSOAPResponseHeader',
    'ArrayAppend': 'ArrayAppend',
    'ArrayAvg': 'ArrayAvg',
    'ArrayClear': 'ArrayClear',
    'ArrayDeleteAt': 'ArrayDeleteAt',
    'ArrayInsertAt': 'ArrayInsertAt',
    'ArrayIsDefined': 'ArrayIsDefined',
    'ArrayIsEmpty': 'ArrayIsEmpty',
    'ArrayLen': 'ArrayLen',
    'ArrayMax': 'ArrayMax',
    'ArrayMin': 'ArrayMin',
    'ArrayNew': 'ArrayNew',
    'ArrayPrepend': 'ArrayPrepend',
    'ArrayResize': 'ArrayResize',
    'ArraySet': 'ArraySet',
    'ArraySort': 'ArraySort',
    'ArraySum': 'ArraySum',
    'ArraySwap': 'ArraySwap',
    'ArrayToList': 'ArrayToList',
    'Asc': 'Asc',
    'ASin': 'ASin',
    'ATan': 'ATan',
    'Beat': 'Beat',
    'BinaryDecode': 'BinaryDecode',
    'BinaryEncode': 'BinaryEncode',
    'BitAnd': 'BitAnd',
    'BitMaskClear': 'BitMaskClear',
    'BitMaskRead': 'BitMaskRead',
    'BitMaskSet': 'BitMaskSet',
    'BitNot': 'BitNot',
    'BitOr': 'BitOr',
    'BitSHLN': 'BitSHLN',
    'BitSHRN': 'BitSHRN',
    'BitXOr': 'BitXOr',
    'Ceiling': 'Ceiling',
    'CFusion_decrypt': 'CFusion_decrypt',
    'CFusion_encrypt': 'CFusion_encrypt',
    'CharsetDecode': 'CharsetDecode',
    'CharsetEncode': 'CharsetEncode',
    'Chr': 'Chr',
    'CJustify': 'CJustify',
    'Compare': 'Compare',
    'CompareNoCase': 'CompareNoCase',
    'CompileRest': 'CompileRest',
    'ComponentInfo': 'ComponentInfo',
    'CompoundHash': 'CompoundHash',
    'ContractPath': 'ContractPath',
    'Cos': 'Cos',
    'CreateDecoder': 'CreateDecoder',
    'CreateObject': 'CreateObject',
    'CreateUUId': 'CreateUUId',
    'CreateODBCDate': 'CreateODBCDate',
    'CreateODBCDateTime': 'CreateODBCDateTime',
    'CreateODBCTime': 'CreateODBCTime',
    'CreateTime': 'CreateTime',
    'CreateTimeSpan': 'CreateTimeSpan',
    'CreateUniqueString': 'CreateUniqueString',
    'DateAdd': 'DateAdd',
    'DateCompare': 'DateCompare',
    'DateConvert': 'DateConvert',
    'DateDiff': 'DateDiff',
    'DateFormat': 'DateFormat',
    'DatePart': 'DatePart',
    'DateTimeFormat': 'DateTimeFormat',
    'Day': 'Day',
    'DayOfWeek': 'DayOfWeek',
    'DayOfWeekAsString': 'DayOfWeekAsString',
    'DayOfYear': 'DayOfYear',
    'DaysInMonth': 'DaysInMonth',
    'DaysInYear': 'DaysInYear',
    'DecrementValue': 'DecrementValue',
    'Decrypt': 'Decrypt',
    'DecryptBinary': 'DecryptBinary',
    'DeleteClientVariable': 'DeleteClientVariable',
    'DESDecrypt': 'DESDecrypt',
    'DESEncrypt': 'DESEncrypt',
    'DirectoryExists': 'DirectoryExists',
    'DollarFormat': 'DollarFormat',
    'Duplicate': 'Duplicate',
    'Each': 'Each',
    'Encrypt': 'Encrypt',
    'EncryptBinary': 'EncryptBinary',
    'EntityDecode': 'EntityDecode',
    'EntityEncode': 'EntityEncode',
    'Exp': 'Exp',
    'ExpandPath': 'ExpandPath',
    'Extract': 'Extract',
    'FileExists': 'FileExists',
    'Find': 'Find',
    'FindNoCase': 'FindNoCase',
    'FindOneOf': 'FindOneOf',
    'FirstDayOfMonth': 'FirstDayOfMonth',
    'Fix': 'Fix',
    'FormatBaseN': 'FormatBaseN',
    'GetApplicationSettings': 'GetApplicationSettings',
    'GetApplicationMetaData': 'GetApplicationMetaData',
    'GetAuthUser': 'GetAuthUser',
    'GetBaseTagData': 'GetBaseTagData',
    'GetBaseTagList': 'GetBaseTagList',
    'GetBaseTemplatePath': 'GetBaseTemplatePath',
    'GetClientVariablesList': 'GetClientVariablesList',
    'GetComponentMetaData': 'GetComponentMetaData',
    'GetContextRoot': 'GetContextRoot',
    'GetCurrentTemplatePath': 'GetCurrentTemplatePath',
    'GetDirectoryFromPath': 'GetDirectoryFromPath',
    'GetEncoding': 'GetEncoding',
    'GetException': 'GetException',
    'GetFileFromPath': 'GetFileFromPath',
    'GetFileInfo': 'GetFileInfo',
    'GetFunctionList': 'GetFunctionList',
    'GetGatewayHelper': 'GetGatewayHelper',
    'GetHttpTimeString': 'GetHttpTimeString',
    'GetK2ServerDocCount': 'GetK2ServerDocCount',
    'GetK2ServerDocCountLimit': 'GetK2ServerDocCountLimit',
    'GetLocale': 'GetLocale',
    'GetLocaleDisplayName': 'GetLocaleDisplayName',
    'GetMetaData': 'GetMetaData',
    'GetMetricData': 'GetMetricData',
    'GetPageContext': 'GetPageContext',
    'GetProfileSections': 'GetProfileSections',
    'GetProfileString': 'GetProfileString',
    'GetRequestData': 'GetRequestData',
    'GetScriptProtectNumLines': 'GetScriptProtectNumLines',
    'GetSOAPRequest': 'GetSOAPRequest',
    'GetSOAPRequestHeader': 'GetSOAPRequestHeader',
    'GetSOAPResponse': 'GetSOAPResponse',
    'GetSOAPResponseHeader': 'GetSOAPResponseHeader',
    'GetTempDirectory': 'GetTempDirectory',
    'GetTempFile': 'GetTempFile',
    'GetTickCount': 'GetTickCount',
    'GetTimeZoneInfo': 'GetTimeZoneInfo',
    'GetToken': 'GetToken',
    'GetTotalSpace': 'GetTotalSpace',
    'GetUserRoles': 'GetUserRoles',
    'GetWriteableImageFormats': 'GetWriteableImageFormats',
    'Hash': 'Hash',
    'Hash40': 'Hash40',
    'Hour': 'Hour',
    'HTMLCodeFormat': 'HTMLCodeFormat',
    'HTMLEditFormat': 'HTMLEditFormat',
    'IIf': 'IIf',
    'ImageAddBorder': 'ImageAddBorder',
    'ImageBlur': 'ImageBlur',
    'ImageClearRect': 'ImageClearRect',
    'ImageCopy': 'ImageCopy',
    'ImageCreateCaptcha': 'ImageCreateCaptcha',
    'ImageCrop': 'ImageCrop',
    'ImageDilate': 'ImageDilate',
    'ImageDrawArc': 'ImageDrawArc',
    'ImageDrawBeveledRect': 'ImageDrawBeveledRect',
    'ImageDrawCubicCurve': 'ImageDrawCubicCurve',
    'ImageDrawLine': 'ImageDrawLine',
    'ImageDrawLines': 'ImageDrawLines',
    'ImageDrawOval': 'ImageDrawOval',
    'ImageDrawPoint': 'ImageDrawPoint',
    'ImageDrawQuadraticCurve': 'ImageDrawQuadraticCurve',
    'ImageDrawRect': 'ImageDrawRect',
    'ImageDrawRoundRect': 'ImageDrawRoundRect',
    'ImageDrawText': 'ImageDrawText',
    'ImageFlip': 'ImageFlip',
    'ImageGetBlob': 'ImageGetBlob',
    'ImageGetBufferedImage': 'ImageGetBufferedImage',
    'ImageGetEXIFTag': 'ImageGetEXIFTag',
    'ImageGetHeight': 'ImageGetHeight',
    'ImageGetIPTCTag': 'ImageGetIPTCTag',
    'ImageGetWidth': 'ImageGetWidth',
    'ImageGrayScale': 'ImageGrayScale',
    'ImageInfo': 'ImageInfo',
    'ImageNegative': 'ImageNegative',
    'ImageNew': 'ImageNew',
    'ImageOverlay': 'ImageOverlay',
    'ImagePaste': 'ImagePaste',
    'ImageRead': 'ImageRead',
    'ImageReadBase64': 'ImageReadBase64',
    'ImageResize': 'ImageResize',
    'ImageRotate': 'ImageRotate',
    'ImageRotateDrawingAxis': 'ImageRotateDrawingAxis',
    'ImageScaleToFit': 'ImageScaleToFit',
    'ImageSetBackgroundColor': 'ImageSetBackgroundColor',
    'ImageSetDrawingColor': 'ImageSetDrawingColor',
    'ImageSetDrawingStroke': 'ImageSetDrawingStroke',
    'ImageSetDrawingTransparency': 'ImageSetDrawingTransparency',
    'ImageSharpen': 'ImageSharpen',
    'ImageShear': 'ImageShear',
    'ImageShearDrawingAxis': 'ImageShearDrawingAxis',
    'ImageTranslate': 'ImageTranslate',
    'ImageTranslateDrawingAxis': 'ImageTranslateDrawingAxis',
    'ImageWrite': 'ImageWrite',
    'ImageWriteBase64': 'ImageWriteBase64',
    'IncrementValue': 'IncrementValue',
    'InputBaseN': 'InputBaseN',
    'Insert': 'Insert',
    'Int': 'Int',
    'InvalidateOAuthaccesstoken': 'InvalidateOAuthaccesstoken',
    'IsArray': 'IsArray',
    'IsBinary': 'IsBinary',
    'IsBoolean': 'IsBoolean',
    'IsCustomFunction': 'IsCustomFunction',
    'IsDate': 'IsDate',
    'IsDDX': 'IsDDX',
    'IsDebugMode': 'IsDebugMode',
    'IsImage': 'IsImage',
    'IsImageFile': 'IsImageFile',
    'IsInstanceOf': 'IsInstanceOf',
    'IsJSON': 'IsJSON',
    'IsLeapYear': 'IsLeapYear',
    'IsNumeric': 'IsNumeric',
    'IsNumericDate': 'IsNumericDate',
    'IsObject': 'IsObject',
    'IsPDFFile': 'IsPDFFile',
    'IsPDFObject': 'IsPDFObject',
    'IsQuery': 'IsQuery',
    'IsSimpleValue': 'IsSimpleValue',
    'IsSOAPRequest': 'IsSOAPRequest',
    'IsStruct': 'IsStruct',
    'IsUserInAnyRole': 'IsUserInAnyRole',
    'IsUserInRole': 'IsUserInRole',
    'IsUserLoggedIn': 'IsUserLoggedIn',
    'IsValid': 'IsValid',
    'IsValidOauthaccesstoken': 'IsValidOauthaccesstoken',
    'IsWDDX': 'IsWDDX',
    'IsXML': 'IsXML',
    'IsXMLAttribute': 'IsXMLAttribute',
    'IsXMLElement': 'IsXMLElement',
    'IsXMLNode': 'IsXMLNode',
    'IsXMLRoot': 'IsXMLRoot',
    'IsXSSFFile': 'IsXSSFFile',
    'IsXSSFPicture': 'IsXSSFPicture',
    'IsXSSFShape': 'IsXSSFShape',
    'IsXSSFSheet': 'IsXSSFSheet',
    'IsXSSFWorkbook': 'IsXSSFWorkbook',
    'JSStringFormat': 'JSStringFormat',
    'LCase': 'LCase',
    'Left': 'Left',
    'Len': 'Len',
    'ListAppend': 'ListAppend',
    'ListChangeDelims': 'ListChangeDelims',
    'ListContains': 'ListContains',
    'ListContainsNoCase': 'ListContainsNoCase',
    'ListDeleteAt': 'ListDeleteAt',
    'ListFilter': 'ListFilter',
    'ListFind': 'ListFind',
    'ListFindNoCase': 'ListFindNoCase',
    'ListFirst': 'ListFirst',
    'ListGetAt': 'ListGetAt',
    'ListInsertAt': 'ListInsertAt',
    'ListLast': 'ListLast',
    'ListLen': 'ListLen',
    'ListPrepend': 'ListPrepend',
    'ListQualify': 'ListQualify',
    'ListReduce': 'ListReduce',
    'ListRemoveDuplicates': 'ListRemoveDuplicates',
    'ListRest': 'ListRest',
    'ListSetAt': 'ListSetAt',
    'ListSort': 'ListSort',
    'ListToArray': 'ListToArray',
    'ListValueCount': 'ListValueCount',
    'ListValueCountNoCase': 'ListValueCountNoCase',
    'LJustify': 'LJustify',
    'LSParseCurrency': 'LSParseCurrency',
    'LSParseDateTime': 'LSParseDateTime',
    'LSParseEuroCurrency': 'LSParseEuroCurrency',
    'LSParseNumber': 'LSParseNumber',
    'Max': 'Max',
    'Metaphone': 'Metaphone',
    'Mid': 'Mid',
    'Min': 'Min',
    'Minute': 'Minute',
    'Month': 'Month',
    'MonthAsString': 'MonthAsString',
    'Now': 'Now',
    'NumberFormat': 'NumberFormat',
    'ObjectEquals': 'ObjectEquals',
    'ObjectLoad': 'ObjectLoad',
    'ObjectSave': 'ObjectSave',
    'OnApplicationEnd': 'OnApplicationEnd',
    'OnApplicationStart': 'OnApplicationStart',
    'OnError': 'OnError',
    'OnMissingMethod': 'OnMissingMethod',
    'OnMissingTemplate': 'OnMissingTemplate',
    'OnRequest': 'OnRequest',
    'OnRequestEnd': 'OnRequestEnd',
    'OnRequestStart': 'OnRequestStart',
    'OnSessionEnd': 'OnSessionEnd',
    'OnSessionStart': 'OnSessionStart',
    'ParagraphFormat': 'ParagraphFormat',
    'ParseDateTime': 'ParseDateTime',
    'ParseNumber': 'ParseNumber',
    'Pi': 'Pi',
    'PreserveSingleQuotes': 'PreserveSingleQuotes',
    'Quarter': 'Quarter',
    'QueryAddColumn': 'QueryAddColumn',
    'QueryAddRow': 'QueryAddRow',
    'QueryColumnArray': 'QueryColumnArray',
    'QueryColumnCount': 'QueryColumnCount',
    'QueryColumnExists': 'QueryColumnExists',
    'QueryColumnList': 'QueryColumnList',
    'QueryConvertForGrid': 'QueryConvertForGrid',
    'QueryCurrentRow': 'QueryCurrentRow',
    'QueryDeleteColumn': 'QueryDeleteColumn',
    'QueryDeleteRow': 'QueryDeleteRow',
    'QueryGetCell': 'QueryGetCell',
    'QueryGetRow': 'QueryGetRow',
    'QueryMap': 'QueryMap',
    'QueryNew': 'QueryNew',
    'QueryRecordCount': 'QueryRecordCount',
    'QueryReduce': 'QueryReduce',
    'QueryRowData': 'QueryRowData',
    'QuerySetCell': 'QuerySetCell',
    'Rand': 'Rand',
    'Randomize': 'Randomize',
    'RandRange': 'RandRange',
    'REFind': 'REFind',
    'REFindNoCase': 'REFindNoCase',
    'ReleaseComObject': 'ReleaseComObject',
    'RemoveChars': 'RemoveChars',
    'RemoveNumeric': 'RemoveNumeric',
    'RepeatString': 'RepeatString',
    'Replace': 'Replace',
    'ReplaceList': 'ReplaceList',
    'ReplaceNoCase': 'ReplaceNoCase',
    'REReplace': 'REReplace',
    'REReplaceNoCase': 'REReplaceNoCase',
    'RESplit': 'RESplit',
    'RESplitNoCase': 'RESplitNoCase',
    'Reverse': 'Reverse',
    'RTrim': 'RTrim',
    'Second': 'Second',
    'SendGatewayMessage': 'SendGatewayMessage',
    'Serialize': 'Serialize',
    'SerializeJSON': 'SerializeJSON',
    'SerializeXML': 'SerializeXML',
    'SessionId': 'SessionId',
    'SessionInvalidate': 'SessionInvalidate',
    'SessionRotate': 'SessionRotate',
    'SessionTimeout': 'SessionTimeout',
    'SetEncoding': 'SetEncoding',
    'SetLocale': 'SetLocale',
    'SetProfileString': 'SetProfileString',
    'SetVariable': 'SetVariable',
    'Sgn': 'Sgn',
    'Sin': 'Sin',
    'SpanExcluding': 'SpanExcluding',
    'SpanIncluding': 'SpanIncluding',
    'SpreadsheetAddAutoFilter': 'SpreadsheetAddAutoFilter',
    'SpreadsheetAddColumn': 'SpreadsheetAddColumn',
    'SpreadsheetAddFreezePane': 'SpreadsheetAddFreezePane',
    'SpreadsheetAddImage': 'SpreadsheetAddImage',
    'SpreadsheetAddInfo': 'SpreadsheetAddInfo',
    'SpreadsheetAddRow': 'SpreadsheetAddRow',
    'SpreadsheetAddRows': 'SpreadsheetAddRows',
    'SpreadsheetAddSplitPane': 'SpreadsheetAddSplitPane',
    'SpreadsheetCreateSheet': 'SpreadsheetCreateSheet',
    'SpreadsheetDeleteColumn': 'SpreadsheetDeleteColumn',
    'SpreadsheetDeleteColumns': 'SpreadsheetDeleteColumns',
    'SpreadsheetDeleteRow': 'SpreadsheetDeleteRow',
    'SpreadsheetDeleteRows': 'SpreadsheetDeleteRows',
    'SpreadsheetFormatCell': 'SpreadsheetFormatCell',
    'SpreadsheetFormatCellRange': 'SpreadsheetFormatCellRange',
    'SpreadsheetFormatColumn': 'SpreadsheetFormatColumn',
    'SpreadsheetFormatColumns': 'SpreadsheetFormatColumns',
    'SpreadsheetFormatRow': 'SpreadsheetFormatRow',
    'SpreadsheetFormatRows': 'SpreadsheetFormatRows',
    'SpreadsheetGetCellComment': 'SpreadsheetGetCellComment',
    'SpreadsheetGetCellFormula': 'SpreadsheetGetCellFormula',
    'SpreadsheetGetCellValue': 'SpreadsheetGetCellValue',
    'SpreadsheetInfo': 'SpreadsheetInfo',
    'SpreadsheetMergeCells': 'SpreadsheetMergeCells',
    'SpreadsheetNew': 'SpreadsheetNew',
    'SpreadsheetRead': 'SpreadsheetRead',
    'SpreadsheetReadBinary': 'SpreadsheetReadBinary',
    'SpreadsheetRemoveSheet': 'SpreadsheetRemoveSheet',
    'SpreadsheetSetActiveSheet': 'SpreadsheetSetActiveSheet',
    'SpreadsheetSetActiveSheetNumber': 'SpreadsheetSetActiveSheetNumber',
    'SpreadsheetSetCellComment': 'SpreadsheetSetCellComment',
    'SpreadsheetSetCellFormula': 'SpreadsheetSetCellFormula',
    'SpreadsheetSetCellValue': 'SpreadsheetSetCellValue',
    'SpreadsheetSetColumnWidth': 'SpreadsheetSetColumnWidth',
    'SpreadsheetSetFooter': 'SpreadsheetSetFooter',
    'SpreadsheetSetHeader': 'SpreadsheetSetHeader',
    'SpreadsheetSetRowHeight': 'SpreadsheetSetRowHeight',
    'SpreadsheetShiftColumns': 'SpreadsheetShiftColumns',
    'SpreadsheetShiftRows': 'SpreadsheetShiftRows',
    'SpreadsheetWrite': 'SpreadsheetWrite',
    'Sqrt': 'Sqrt',
    'StripCR': 'StripCR',
    'StructAppend': 'StructAppend',
    'StructClear': 'StructClear',
    'StructCopy': 'StructCopy',
    'StructCount': 'StructCount',
    'StructDelete': 'StructDelete',
    'StructEach': 'StructEach',
    'StructFilter': 'StructFilter',
    'StructFind': 'StructFind',
    'StructFindKey': 'StructFindKey',
    'StructFindValue': 'StructFindValue',
    'StructGet': 'StructGet',
    'StructInsert': 'StructInsert',
    'StructIsEmpty': 'StructIsEmpty',
    'StructKeyArray': 'StructKeyArray',
    'StructKeyExists': 'StructKeyExists',
    'StructKeyList': 'StructKeyList',
    'StructNew': 'StructNew',
    'StructSort': 'StructSort',
    'StructUpdate': 'StructUpdate',
    'Tan': 'Tan',
    'Throw': 'Throw',
    'TimeFormat': 'TimeFormat',
    'ToBase64': 'ToBase64',
    'ToBinary': 'ToBinary',
    'ToScript': 'ToScript',
    'ToString': 'ToString',
    'Trace': 'Trace',
    'TransactionCommit': 'TransactionCommit',
    'TransactionRollback': 'TransactionRollback',
    'Trim': 'Trim',
    'UCase': 'UCase',
    'URLDecode': 'URLDecode',
    'URLEncodedFormat': 'URLEncodedFormat',
    'URLSessionFormat': 'URLSessionFormat',
    'Val': 'Val',
    'ValueArray': 'ValueArray',
    'ValueList': 'ValueList',
    'VerifyClient': 'VerifyClient',
    'Week': 'Week',
    'Wrap': 'Wrap',
    'WriteBody': 'WriteBody',
    'WriteDump': 'WriteDump',
    'WriteLog': 'WriteLog',
    'WriteOutput': 'WriteOutput',
    'WSGetAllChannels': 'WSGetAllChannels',
    'WSGetSubscribers': 'WSGetSubscribers',
    'WSPublish': 'WSPublish',
    'WSSendMessage': 'WSSendMessage',
    'WSSubscribe': 'WSSubscribe',
    'XMLChildPos': 'XMLChildPos',
    'XMLElemNew': 'XMLElemNew',
    'XMLFormat': 'XMLFormat',
    'XMLGetNodeType': 'XMLGetNodeType',
    'XMLNew': 'XMLNew',
    'XMLParse': 'XMLParse',
    'XMLSearch': 'XMLSearch',
    'XMLTransform': 'XMLTransform',
    'XMLValidate': 'XMLValidate',
    'Year': 'Year',
    'YesNoFormat': 'YesNoFormat'
  }

  def __init__(self, value, line, col):
    super().__init__(value, line, col)
    self.function = self.FUNCTIONS.get(value)
    
  def __str__(self):
    return f'CFFunctionToken({self.function})' if self.function else 'CFFunctionToken(UNKNOWN)'

class CFScriptToken(CFToken):

  def __init__(self, value, line, col):
    # Validate script token format
    if not value.startswith('<cfscript>') or not value.endswith('</cfscript>'):
      raise ValueError('Invalid script token format')

    super().__init__(value, line, col)
    self.script = value[10:-11].strip()

  def _get_script(self, value):
    if value.startswith('<cfscript>') and value.endswith('</cfscript>'):
      return value[10:-11].strip()
    else:
      return None
    
  def __str__(self):
    script = self.script[:20] if self.script else 'INVALID'
    return f'CFScriptToken({script}...)'

class CFTokenizer:

  def __init__(self, code):
    self.code = code
    self.tokens = []

  def tokenize(self):
    lines = self.code.split('\n')
    
    for line_num, line in enumerate(lines, start=1):
      self.tokenize_line(line, line_num)

    return self.tokens

  def tokenize_line(self, text, line_num):
    self.tokenize_tags(text, line_num)
    self.tokenize_strings(text, line_num)
    self.tokenize_keywords(text, line_num)
    self.tokenize_operators(text, line_num)
    self.tokenize_functions(text, line_num)
    self.tokenize_script(text, line_num)

  def tokenize_tags(self, text, line):
    for match in CFTagToken.TAG_REGEX.finditer(text):
      token = CFTagToken(match.group(), line, match.start()+1)
      self.tokens.append(token)

  def tokenize_strings(self, text, line):
    for match in CFStringToken.STRING_REGEX.finditer(text):
      token = CFStringToken(match.group(), line, match.start()+1)
      self.tokens.append(token)

  def tokenize_keywords(self, text, line):
    for word in CFKeywordToken.KEYWORDS:
      idx = text.find(word)
      if idx != -1:
        token = CFKeywordToken(word, line, idx+1)
        self.tokens.append(token)

  def tokenize_operators(self, text, line):
    for op in CFOperatorToken.OPERATORS:
      idx = text.find(op)
      if idx != -1:
        token = CFOperatorToken(op, line, idx+1)
        self.tokens.append(token)
        
  def tokenize_functions(self, text, line):
    if not isinstance(text, str):
      return
    
    for func in CFFunctionToken.FUNCTIONS:
      idx = text.find(func)
      if idx != -1:
        token = CFFunctionToken(func, line, idx+1)
        self.tokens.append(token)

  def tokenize_script(self, text, line):
    idx = text.find('<cfscript>')
    if idx != -1:
      script = text[idx+10:-11]
      token = CFScriptToken(script, line, idx+1)
      self.tokens.append(token)