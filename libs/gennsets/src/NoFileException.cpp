// Copyright 2008,2009,2010,2011 Loïc Cerf (magicbanana@gmail.com)

// This file is part of gennsets.

// gennsets is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License version 3 as published by the Free Software Foundation

// gennsets is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

// You should have received a copy of the GNU General Public License along with gennsets; if not, write to the Free Software Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA

#include "NoFileException.h"

NoFileException::NoFileException(): fileName("")
{
}

NoFileException::NoFileException(const char* fileNameParam): fileName(fileNameParam)
{
}

NoFileException::~NoFileException() throw()
{
}

const char* NoFileException::what() const throw()
{
  return (fileName + " cannot be opened!").c_str();
}
